from google.cloud import translate,translate_v2
import os
from google.oauth2 import service_account
import six
from google.cloud import translate_v2 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"
def detect_language(text):
    """Detects the text's language."""

    translate_client = translate_v2.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print("Text: {}".format(text))
    print("Confidence: {}".format(result["confidence"]))
    return result["language"]

def translate_text(text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    

    translate_client = translate_v2.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language='en')

    return result["translatedText"]
 
