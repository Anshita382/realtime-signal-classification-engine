##  Final `README.MD`

```md
# ANSHITA RAYALLA – UFO SIGHTING ANALYZER

**Course**: CIS 6930 – Spring 2025  
**Project**: 3 – Analyzing Sighting  
**GitHub Repository**: https://github.com/Anshita382/cis6930sp25-project3

---

## 🛸 PROJECT SUMMARY

This project is the final stage of a data engineering pipeline that intercepts and analyzes potential alien communications.  
The system connects to a RabbitMQ server, classifies incoming messages as **alien 👽** or **human**, and generates four visual PDF reports using real-time message data.

You were promoted to a field agent in the Extraterrestrial Data Analysis Department (EDAD), and this tool helps analyze UFO sightings broadcasted over Earth networks.

---

## 🔧 FEATURES

- **RabbitMQ Integration** using fanout exchange to receive messages
- **Alien/Human Classification** using simple NLP pattern detection
- **Loguru Logging** to track message flow and classification results
- **Four Visual Reports** saved as PDF in the `output/` folder:
  - `report1.pdf`: Map of sighting locations
  - `report2.pdf`: Shape frequency over time
  - `report3.pdf`: Shape distribution
  - `report4.pdf`: Alien vs. Human message count
- **Container-ready** via `apptainer.def`
- **Test coverage** using `pytest`

---

## HOW TO RUN

### 1. Clone the Repository
```bash
git clone https://github.com/Anshita382/cis6930sp25-project3.git
cd cis6930sp25-project3
```

### 2. Set Up the Python Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the Application (Local Test)
```bash
PYTHONPATH=src python main.py --command 'localhost' --port 5672
```

### 4. Run the Application (RabbitMQ Live)
```bash
python main.py --command 'cpu002.cm.cluster' --port 5672
```

### 5. Run Unit Tests
```bash
PYTHONPATH=src pytest -v
```

---

##  CONTAINER USAGE

### Build with Apptainer
```bash
apptainer build edad.sif apptainer.def
```

### Run from Container
```bash
apptainer run edad.sif --command 'cpu002.cm.cluster' --port 5672
```

---

## 📁 PROJECT STRUCTURE

```
cis6930sp25-project3/
├── main.py
├── apptainer.def
├── pyproject.toml
├── requirements.txt
├── README.MD
├── COLLABORATORS.md
├── src/
│   └── edad/
│       ├── consumer.py
│       ├── classifier.py
│       ├── logger.py
│       ├── visualizer.py
│       └── __init__.py
├── tests/
│   └── test_classifier.py
├── output/
│   ├── edad.log
│   ├── report1.pdf
│   ├── report2.pdf
│   ├── report3.pdf
│   └── report4.pdf
```

---

## ASSUMPTIONS / BUGS

- Messages are assumed to be valid JSON with all required fields
- Classification is rule-based (no ML): at least 2 known English words = human
- If RabbitMQ is unreachable, fallback test messages are used
- Matplotlib may not render 👽 emoji in PDFs (font missing)
- Pandas `to_datetime()` may emit a warning for Unix timestamps

---

## AUTHOR

**Anshita Rayalla**  
MS in Computer Science  
University of Florida (Fall 2024 – Spring 2026)  

```
