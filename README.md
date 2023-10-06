# esd

## About the Project

An application to monitor and prescribe run-based conditioning workouts for athletes.

See the following [blog post](https://michaelwknott.github.io/monitoring-and-prescribing-individualised-conditioning-sessions-part-1.html) for the project overview.

### Built With

+ [Python](https://www.python.org/)
+ [Rich](https://rich.readthedocs.io/en/stable/introduction.html)

## Getting Started

### Prerequisites

- Python >= 3.11

### Installation

1. Clone the repo
   ```bash
   git clone git@github.com:michaelwknott/esd.git
   ```
2. Create a virtual environment
   ```bash
   python -m venv .venv --prompt .
   ```
3. Activate virtual environment
    ```bash
    source .venv/bin/activate
    ```
4. Install dependencies
    ```bash
    python -m pip install -r requirements.txt
    ```

## Usage

1. Run the application
    ```bash
    python -m esd
    ```
2. Follow the prompts to select and prescribe a workout
    ```bash
    Available workouts:
    1. Passive Long Intervals - Normal: 2 mins work / 2 mins rest
    2. Passive Long Intervals - Extensive: 2 mins work / 1 mins rest
    3. Passive Long Intervals - Intensive: 2 mins work / 3 mins rest
    Select a workout:
    ```
3. View the prescribed workout in the terminal
    ```bash
    Passive Long Intervals - Normal: 2 mins work / 2 mins rest -
                            23/08/2023
    ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
    ┃ Athlete Name     ┃ Work Distance (m) ┃ Rest Distance (m) ┃
    ┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
    │ John Doe         │      470.0m       │       0.0m        │
    │ Jane Smith       │      522.0m       │       0.0m        │
    │ Michael Johnson  │      490.0m       │       0.0m        │
    │ Sarah Thompson   │      462.0m       │       0.0m        │
    │ David Miller     │      444.0m       │       0.0m        │
    │ Emily Wilson     │      500.0m       │       0.0m        │
    │ James Anderson   │      452.0m       │       0.0m        │
    │ Sophia Kelly     │      511.0m       │       0.0m        │
    │ Matthew Wright   │      437.0m       │       0.0m        │
    │ Olivia Brown     │      462.0m       │       0.0m        │
    │ Adam Wilson      │      470.0m       │       0.0m        │
    │ Sophie Turner    │      490.0m       │       0.0m        │
    │ Benjamin Davis   │      444.0m       │       0.0m        │
    │ Emma Clark       │      500.0m       │       0.0m        │
    │ Maxwell Thompson │      452.0m       │       0.0m        │
    │ Sophia Davis     │      511.0m       │       0.0m        │
    │ Daniel Brown     │      480.0m       │       0.0m        │
    │ Ella Wilson      │      452.0m       │       0.0m        │
    │ Jacob Turner     │      470.0m       │       0.0m        │
    │ Sophia Hill      │      490.0m       │       0.0m        │
    │ Liam Adams       │      500.0m       │       0.0m        │
    └──────────────────┴───────────────────┴───────────────────┘
    ```

## License

Distributed under the MIT License. See LICENSE for more information.
