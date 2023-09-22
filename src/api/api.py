import datetime
import json

from bottle import BaseRequest, HTTPError, HTTPResponse, error, get, post, request, run
from src.api.main import API_VERSION, MODEL_NAME, process_query
from src.logger import init_logger

PORT = 8090

BaseRequest.MEMFILE_MAX = 1024 * 1024 * 1024
logger = init_logger('api', log_file=False)


@get('/answer')
def get_answer():
    """
    Get answer of the provided query

    Parameters:
        quwery (str): query string

    Returns:
        response (dict): API response (see readme) containing answer(str), source(str) and metadata
    """
    if not request.json:
        return HTTPResponse({'Empty request was given.'}, 400)

    response = process_query(request.json)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Response received at {current_time}")

    return response


@get('/settings')
def get_settings():
    """
    Get settings for the current api
    (model name, api version)

    Returns:
        response (dict): Settings response
    """
    return json.dumps({
        'api_version': API_VERSION,
        'model_name': MODEL_NAME
    })


def main():
    run(host='0.0.0.0', port=PORT, server='paste')
    logger.info('API running ...')


@error(404)
def error404():
    return json.dumps({'error': 'URL not found'})


@error(500)
def error500(http_error: HTTPError):
    return json.dumps({'error': [line.strip() for line in http_error.traceback.split('\n') if len(line.strip()) > 0]})


if __name__ == '__main__':
    main()
