import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ✅ Sample dataset with balanced labels
data = {
    'label': ['ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam'],
    'message': [
        "Let's catch up over lunch tomorrow.",
        "Congratulations! You've won a $1000 Walmart gift card. Click here.",
        "Are you free this weekend?",
        "Get cheap loans instantly at low interest rates!",
        "Can you send the meeting notes?",
        "URGENT! Your account has been compromised. Click now to secure.",
        "Let's study together today.",
        "You've been selected for a free trip to Maldives!",
        "Please bring your ID card.",
        "Claim your free reward now!"
    ]
}

# 🧾 Create dataframe
df = pd.DataFrame(data)

# 🔄 Label encoding
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 🧪 Split features and labels
X = df['message']
y = df['label']

# 🧠 Text vectorization
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# ✂ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.3, random_state=42)

# 🤖 Naive Bayes Model
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)

print("🔍 Naive Bayes Results:")
print("Accuracy:", accuracy_score(y_test, nb_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, nb_pred))
print("Classification Report:\n", classification_report(y_test, nb_pred, zero_division=0))

# 🤖 SVM Model
svm_model = SVC()
svm_model.fit(X_train, y_train)
svm_pred = svm_model.predict(X_test)

print("\n🔍 SVM Results:")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, svm_pred))
print("Classification Report:\n", classification_report(y_test, svm_pred, zero_division=0))
