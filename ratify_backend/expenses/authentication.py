from types import SimpleNamespace
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin
from firebase_admin import credentials, auth
import os

FIREBASE_KEY_PATH = os.environ.get("FIREBASE_KEY_PATH", r"C:\1\repos\ratify-server\ratify_backend\serviceAccountKey.json")

def initialize_firebase():
    try:
        if not firebase_admin._apps:
            if os.path.exists(FIREBASE_KEY_PATH):
                print(f"Initializing Firebase with key at: {FIREBASE_KEY_PATH}")
                cred = credentials.Certificate(FIREBASE_KEY_PATH)
                firebase_admin.initialize_app(cred)
            else:
                print(f"Service account key not found at: {FIREBASE_KEY_PATH}")
                raise FileNotFoundError("Service account key file not found")
    except Exception as e:
        print(f"Error initializing Firebase: {str(e)}")
        raise

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            return None

        id_token = auth_header.split(" ").pop()
        try:
            initialize_firebase()
            decoded_token = auth.verify_id_token(id_token)
            if not decoded_token:
                return None

            # Wrap it in a simple object to satisfy DRF
            user = SimpleNamespace(
                uid=decoded_token.get("uid"),
                email=decoded_token.get("email", ""),
                is_authenticated=True
            )

            request.firebase_user = decoded_token  # still keep the raw token for manual access
            return (user, None)

        except Exception as e:
            print(f"Firebase authentication error: {str(e)}")
            raise exceptions.AuthenticationFailed('Invalid token')

    def authenticate_header(self, request):
        return 'Bearer'
