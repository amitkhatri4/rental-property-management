from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Simple view to handle chatbot requests
@csrf_exempt  # To allow POST requests without CSRF token for testing
def ask_chatbot(request):
    if request.method == "POST":
        try:
            # Get the message sent by the user
            user_message = request.POST.get('message', '')

            # You can now integrate your chatbot logic here.
            # For example, using a basic response:
            bot_response = "I am a chatbot! You said: " + user_message

            # Returning the response as JSON
            return JsonResponse({"response": bot_response})
        except Exception as e:
            return JsonResponse({"response": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"response": "Invalid request method!"}, status=400)
