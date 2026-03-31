# 🐝 Bee Content Review System

A Streamlit web app for the **Bee Mentorship** marketing team to submit Instagram content and verify it against brand guidelines before publishing.

---

## ✨ Features

| Feature | Details |
|---|---|
| **Media upload** | Upload images (JPG, PNG, GIF) or videos (MP4, MOV, AVI) |
| **Caption editor** | Write and review post captions with a live character counter |
| **Brand checklist** | Six-point compliance checklist covering design & tone |
| **Automatic scoring** | Percentage score based on checklist completion |
| **Smart feedback** | *Perfect*, *Almost there*, or *Needs improvement* |
| **Pastel UI** | Clean, aesthetic interface with soft warm colors |

### Brand Guidelines Checklist

- 🎨 Brand colors used (honey yellow, warm white, deep brown, coral)
- 🔤 Correct fonts used (Futura / Avenir)
- 🖼️ Logo placement and spacing respected
- 📐 Reel safe zone respected
- ✨ Approved graphics / assets used
- 💬 Caption tone is warm and human

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/shaikmaazahammed/bee-content-review-system.git
cd bee-content-review-system

# 2. (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
bee-content-review-system/
├── app.py            # Main Streamlit application
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 🛠️ Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web application framework |
| `Pillow` | Image preview rendering |

---

## 📖 How to Use

1. **Upload** your image or video using the file uploader.
2. **Write** your Instagram caption in the text area.
3. **Tick** every brand guideline item that applies to your content.
4. Click **🐝 Submit for Review** to see your score and feedback.
5. Address any unchecked items highlighted in the results section.

---

## 🎨 Design

The UI uses a warm pastel colour palette inspired by the Bee Mentorship brand:

| Role | Colour |
|---|---|
| Background | `#FFF9F0` – warm cream |
| Accent / borders | `#FFB347` – honey yellow |
| Header gradient | `#FFE0A3` → `#FFD6E0` |
| Score card | `#D4F1C0` → `#B5E8D0` |

---

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in this repository.
