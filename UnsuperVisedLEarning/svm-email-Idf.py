from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#  Sample Email Dataset (Text + Labels)
emails = [
    "Congratulations! You won a lottery of $10,000",
    "Get cheap loans now!",
    "Hey, are we still meeting tomorrow?",
    "Earn money fast, work from home!",
    "Let's catch up over lunch",
    "Limited time offer, click now!",
    "Meeting rescheduled to 3 PM",
    "You are selected for a prize, click the link!",
    "Don't forget to bring documents",
    "This is not a spam email"
]

labels = [1, 1, 0, 1, 0, 1, 0, 1, 0, 0]  # 1 = spam, 0 = not spam

#  Vectorization (Text => Numeric Features)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)  # Convert all emails to TF-IDF vectors
y = labels

#  Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#  SVM Model
model = SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)

# Prediction on test data
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))


new_email = [" Congratulation sid"]
new_email_vector = vectorizer.transform(new_email)  # Use the same vectorizer
prediction = model.predict(new_email_vector)

print("New email is:", "Spam" if prediction[0] == 1 else "Not Spam")

