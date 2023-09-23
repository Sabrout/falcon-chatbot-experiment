# WeLoop Chatbot

Bases on files extracted from the WeLoop knowledge base, I developed a conversational agent, based on the language model Falcon-7B and OpenAI's GPT 3.5 turbo, enabling a user to ask questions about the Weloop tool. If a relevant resource exists, it will be proposed to the user, otherwise the model will try to understand the user's problem or question in order to formulate a summary for Weloop customer support.

# Contact

The whole project is pushed into a private GitHub reposotiry (in case the test content is confidential). If you have any questions, difficulties installing or running the project, please reach out to me on <omarsabrout@gmail.com>.

# Remarks

In this section, I explain and show the components of the project alongside the documentation within the code.

## Structure

    .
    ├── config                   # Pre-defined configurations
    │   ├── api-config.json      # Configuration parameters for the API to load
    │   └── openai-config.json   # OpenAI credentials
    ├── data                     # Initial WeLoop data for the model
    │   └── text                 # Contextual text data provided by WeLoop
    │   └── db                   # Preprocessed version of WeLoop data
    ├── log                      # Auto-generated logs
    ├── src                      # Source code
    │   ├── api                  # API code
    │   │   ├── api.py           # Run API
    │   │   └── main.py          # API request processing functions
    │   ├── jupyter              # Notebooks to run examples of language models
    │   └──logger.py             # Custom logger
    ├── Dockerfile               # Build a docker image of the project
    ├── README.md
    ├── REPONSES.md              # Answers to the requested questions in the technical test
    └── requirements.txt         # Python environement packages


## Model Selection

In the vast domain of machine learning, there are many LLM MODELS that can be applied in this case and many of them will do just fine. As a result, I decided to use OpenAI for the API to have a reasonable response time for the API. However, I also provided a jupyter notebook with Faclon-7B-Instruct as it's widely accepted as the best performing open-source model with a public licence. Any other choice of model would be purly dependant on its performance and the available hardware.

## Quantization

As for the sake of this task, I've decided to run the model in 4-bits as I don't have a machien powerful enough to run it in full capacity. It's also the reason why I selected other parameters to limit the demand of such a model. Hence, I selected the 7B version instead of 30B.

## OS Compatibility

One of the greatest concerns when it comes to Python on different operating systems is path handling. So, all paths used in the project are passed through pathlib.Path() to avoid backslash/forwardslash issues between Windows and Linux.

## Possible Improvements

### API instead of Python package:

A more production friendly approach would be deploying the model in an API that handles the user queries within a certain period of time (1 min for example). This API can then be queried by user app interfaces or other frontends.

Thus, I implemented an API withint the project to demonstrate this improvement.

### Model Tuning:

Since this task is intended for evaluation rather than production, the provided Falcon model isn't performing as well as it should. There are evaluation standards that it does not meet. For example, it does not provide accurate answers regarding the WeLoop data and it sometimes responds in Englsih instead of French.

### Containerize

While Python scripts run arguably on any machine that has Python installed, a common practice is adopted in production to use Docker containers since it will probably be deployed on a remote server. These containers require Docker images so

Hence, I implemented a Dockerfile that builds an image (provided Docker is installed on the host machine) using the command:

```bash
docker build -t [image_name] .
```

Where **[image_name]** can be "bot-detection-image" for example. Then we run image using the command:

```bash
docker run --rm -it --entrypoint bash [image_name]
```

After running the image, we proceed to either run the CSV prediction script or run the API as explained in the coming sections. We can skip the installation section since it is already included in Dockerfile.

# Installation

To install the project, Python 3.10 or higher is required and it is recommended to have an empty Python environment. I personally use Anaconda to handle Python environments. To start, download the provided ZIP archive and extract it. Then, install essential packages by the command:

```bash
cd [project_path]
pip install -r requirements.txt
```

Where **[project_path]** is the absolute path of the extracted archive directory. Now the project is ready to be executed.


# Run API

Run command:

```bash
python -m src.api.api
```

API will be running on http://0.0.0.0:8090.

## Example Request

```json
// GET http://0.0.00:8090/answer
// Request body in raw JSON
{
    "query": "Qu'est-ce que WeLoop presente ?"
}
```

## Example Response

```json
{
  "answer": "WeLoop présente une plateforme Saas basée sur la communauté et l'expérience utilisateur. Elle propose une solution comportant deux interfaces : une interface pour les utilisateurs finaux (Widget) et une interface pour les administrateurs (Back Office).\n\nL'interface pour les utilisateurs finaux s'intègre facilement à vos applications métier. Elle permet aux utilisateurs de participer à des projets, de donner leur avis, de partager des idées et de collaborer avec d'autres membres de la communauté.\n\nL'interface pour les administrateurs leur permet de gérer les projets et les interactions. Il existe deux niveaux d'administrateurs : les Super Admin qui ont accès à tous les projets au sein de l'organisation, et les Admin qui sont les responsables opérationnels d'un ou plusieurs projets.\n\nEn résumé, WeLoop permet de créer une communauté d'utilisateurs engagés, de recueillir leurs retours et de favoriser la collaboration pour améliorer vos produits et services.",
    "source": [
        "data/text/WeLoop c_est quoi _.txt"
    ],
    "metadata": {
        "model_version": "GPT3.5-turbo",
        "api_version": 1.0
    }
}
```
