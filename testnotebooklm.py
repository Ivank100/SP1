# notebooklm.py
from src.rag_query import answer_question

# 🔧 Replace these with your real doc_ids:
PDF_DOC_ID = "e3f9d4c0-dff5-4ee7-af6e-bbfd7866d1fe"   # <- your PDF doc_id
AUDIO_DOC_ID = "ae094b7b-7c5e-48ba-9c77-7ae52490ce66"                # <- fill in after ingest


def chat_session(label: str, doc_id: str):
    """
    Start a simple chat session restricted to a single doc_id.
    """
    print(f"\n=== Chatting with {label} (doc_id={doc_id}) ===")
    print("Press ENTER on an empty line to return to menu.\n")

    while True:
        q = input("Q: ").strip()
        if not q:  # empty line → exit this chat session
            print("\nLeaving session...\n")
            return

        print("\nThinking...\n")
        try:
            answer = answer_question(q, top_k=5, doc_ids=[doc_id])
        except Exception as e:
            print(f"⚠️ Error: {e}")
            continue

        print("Answer:\n")
        print(answer)
        print("\n----------------------------------------\n")


def main_menu():
    while True:
        print("===================================")
        print(" Select document to chat with")
        print("===================================")
        print("  1) PDF only")
        print("  2) Audio only")
        print("  3) Quit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            chat_session("PDF", PDF_DOC_ID)

        elif choice == "2":
            chat_session("Audio", AUDIO_DOC_ID)

        elif choice == "3":
            print("Goodbye!")
            return

        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main_menu()
