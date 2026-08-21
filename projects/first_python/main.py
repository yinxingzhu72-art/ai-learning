from tutor import run_tutor
from profile import load_profile


if __name__ == "__main__":

    user_profile = load_profile()

    run_tutor(user_profile)