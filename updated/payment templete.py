<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment</title>
    <script src="https://js.stripe.com/v3/"></script>
</head>
<body>
    <h1>Make a Payment</h1>
    <form method="POST" id="payment-form">
        {% csrf_token %}
        <div id="card-element">
            <!-- A Stripe Element will be inserted here. -->
        </div>
        <button type="submit">Pay</button>
    </form>

    <script>
        var stripe = Stripe("{{ publishable_key }}");
        var elements = stripe.elements();
        var style = {
            base: {
                fontSize: '16px',
                color: '#32325d',
                lineHeight: '24px',
                fontFamily: 'Helvetica Neue, Helvetica, sans-serif',
            }
        };
        var card = elements.create("card", {style: style});
        card.mount("#card-element");

        var form = document.getElementById("payment-form");
        form.addEventListener("submit", function(event) {
            event.preventDefault();
            stripe.createToken(card).then(function(result) {
                if (result.error) {
                    alert(result.error.message);
                } else {
                    var token = result.token.id;
                    var form = document.createElement("form");
                    form.setAttribute("method", "POST");
                    form.setAttribute("action", "{% url 'payment' %}");

                    var tokenInput = document.createElement("input");
                    tokenInput.setAttribute("type", "hidden");
                    tokenInput.setAttribute("name", "stripeToken");
                    tokenInput.setAttribute("value", token);

                    form.appendChild(tokenInput);
                    document.body.appendChild(form);
                    form.submit();
                }
            });
        });
    </script>
</body>
</html>
