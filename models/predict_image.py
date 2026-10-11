
from pathlib import Path
import sys

import joblib
import numpy as np
from PIL import Image, UnidentifiedImageError
from skimage.color import rgb2gray
from skimage.feature import hog


# ============================================
# PATHS AND SETTINGS
# ============================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "models" / "prosopis_classifier.joblib"

# Predictions below this threshold are marked uncertain.
REVIEW_THRESHOLD = 0.60

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


# ============================================
# IMAGE FEATURE EXTRACTION
# Must match the training code exactly.
# ============================================

def extract_features(image_path, image_size):
    with Image.open(image_path) as original:
        image = original.convert("RGB").resize(tuple(image_size))

    pixels = np.asarray(image)
    gray = rgb2gray(pixels)

    hog_features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm="L2-Hys",
    )

    rgb = pixels.astype(np.float32) / 255.0
    colour_features = []

    for channel in range(3):
        histogram, _ = np.histogram(
            rgb[:, :, channel],
            bins=16,
            range=(0, 1),
            density=True,
        )
        colour_features.extend(histogram)

    return np.concatenate(
        [hog_features, np.asarray(colour_features)]
    ).reshape(1, -1)


# ============================================
# MAIN PREDICTION
# ============================================

def main():
    print("\n===================================")
    print("SUSTAINX - PROSOPIS IMAGE CHECK")
    print("===================================")

    # Check command-line argument
    if len(sys.argv) != 2:
        print(
            '\nUsage:\npython models\\predict_image.py "FULL_IMAGE_PATH"'
        )
        return

    image_path = Path(sys.argv[1]).expanduser()

    if not image_path.is_file():
        print(f"\nERROR: Image file not found:\n{image_path}")
        return

    if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
        print("\nERROR: Unsupported image format.")
        print("Use JPG, JPEG, PNG, BMP, or WEBP.")
        return

    if not MODEL_PATH.is_file():
        print(f"\nERROR: Trained model not found:\n{MODEL_PATH}")
        print("Run: python models\\train_ml_model.py")
        return

    # Load saved model
    try:
        saved = joblib.load(MODEL_PATH)

        model = saved["model"]
        classes = saved["classes"]
        image_size = saved["image_size"]

    except Exception as error:
        print(f"\nERROR: Could not load the trained model:\n{error}")
        return

    # Read and process image
    try:
        features = extract_features(image_path, image_size)

    except (UnidentifiedImageError, OSError, ValueError) as error:
        print(f"\nERROR: Could not read or process the image:\n{error}")
        return

    except Exception as error:
        print(f"\nERROR: Feature extraction failed:\n{error}")
        return

    # Check feature compatibility
    expected_features = getattr(model, "n_features_in_", None)

    if expected_features is not None and features.shape[1] != expected_features:
        print("\nERROR: Image features do not match the trained model.")
        print("Retrain using the current training script.")
        return

    # Predict
    try:
        predicted_class = int(model.predict(features)[0])
        probabilities = model.predict_proba(features)[0]

        class_names = {
            int(label): name
            for name, label in classes.items()
        }

        if predicted_class not in class_names:
            print("\nERROR: Unknown class in model.")
            return

        class_index = list(model.classes_).index(predicted_class)
        score = float(probabilities[class_index])
        label = class_names[predicted_class]

    except Exception as error:
        print(f"\nERROR: Prediction failed:\n{error}")
        return

    # Display cautious result
    print(f"\nImage: {image_path.name}")
    print(f"Model-selected class: {label}")
    print(f"Model score: {score * 100:.2f}%")

    if score < REVIEW_THRESHOLD:
        print("\nRESULT: UNCERTAIN")
        print("ACTION: Send for manual review.")

    elif label == "prosopis":
        print("\nRESULT: POSSIBLE PROSOPIS JULIFLORA")
        print("ACTION: Officer verification required.")

    else:
        print("\nRESULT: POSSIBLE NOT PROSOPIS JULIFLORA")
        print("ACTION: Officer verification required.")

    print("\nIMPORTANT:")
    print("- The model score is not overall test accuracy.")
    print("- A high score does not guarantee a correct prediction.")
    print("- This model needs evaluation on unseen labelled images.")
    print("- Do not use this result as the sole basis for field action.")
    print("\n===================================")


if __name__ == "__main__":
    main()
