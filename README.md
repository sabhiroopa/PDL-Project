# KARUVELAM360 – Prosopis Juliflora Management Platform

## Overview

SUSTAINX is a student-developed prototype designed to support the monitoring and management of invasive Prosopis Juliflora vegetation. The platform aims to help users record affected sites, organize clearance activities, document field evidence, monitor regrowth, and support data-driven environmental management.

The project aligns with Environment & Sustainability and AI, GIS & Emerging Technologies.

## Problem Statement

Managing invasive vegetation requires reliable site records, coordinated clearance activities, evidence of completed work, and continued monitoring to identify regrowth. SUSTAINX explores how digital mapping, structured records, and image-based analysis can support these activities.

## Key Features

- Site registration and management
- Geographic site visualization using GIS mapping
- Site risk and clearance status tracking
- Before-and-after photographic evidence
- Experimental image classification for decision support
- Monitoring and regrowth records
- Budget and biomass tracking
- Alerts, project tracking, and reporting

Feature availability depends on the current prototype implementation.

## Technology Stack

- Python
- Streamlit
- Pandas and CSV
- Leaflet and OpenStreetMap
- GeoJSON
- Pillow
- Scikit-learn and scikit-image for experimental image classification
- Joblib for model storage

## Project Architecture

1. **User interface:** Streamlit provides the application interface.
2. **Application logic:** Python handles site management, monitoring, and project workflows.
3. **Data layer:** CSV files store prototype records, while GeoJSON supports geographic data.
4. **Mapping layer:** Leaflet and OpenStreetMap display geographic information.
5. **Image analysis:** A prototype machine-learning pipeline extracts image features and classifies images.
6. **Monitoring and reporting:** Recorded site information supports follow-up activities and reporting.

## Project Structure

```text
PDL-Project/
├── app.py
├── data/
├── models/
├── images/
├── dataset/
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

Some folders or files may remain local and may not be included in the public repository.

## Installation and Setup

### Prerequisites

- Python 3.12 recommended
- Git
- A compatible terminal

### Install dependencies

Clone the repository:

```bash
git clone https://github.com/sabhiroopa/PDL-Project.git
cd PDL-Project
```

Install the dependencies listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

### Run the application

```bash
python -m streamlit run app.py
```

Open the local address displayed in the terminal.

## Machine-Learning Limitations

The image-classification component is experimental. Its predictions have not yet been established as reliable for field deployment. A prediction score is not the same as validated model accuracy. Results require further testing using a larger, correctly labelled dataset and independent evaluation.

Image predictions should not be used as the sole basis for clearance decisions. Field verification by a responsible person is required.

## Expected Social Impact

SUSTAINX aims to support better environmental monitoring, more traceable clearance activities, improved follow-up of affected sites, and evidence-based planning. Actual impact must be established through field testing and measurable results.

## Future Improvements

- Expand and validate the labelled image dataset
- Evaluate the classifier using independent test data
- Improve monitoring and regrowth alerts
- Strengthen reporting and geographic analytics
- Test usability with intended users
- Evaluate performance through field trials

## Responsible Use of AI

AI-assisted tools were used during parts of the development process for coding support, debugging, and documentation. The team is responsible for reviewing, testing, and validating the submitted work. Any additional AI-generated content or tools used should be disclosed accurately in the competition submission.

## Team

**Team:** SUSTAINX

The project was developed as a student prototype for environmental management and sustainability.

## License

This project is released under the MIT License. See the `LICENSE` file for details.
