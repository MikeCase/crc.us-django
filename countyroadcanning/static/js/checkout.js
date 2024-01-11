document.addEventListener('DOMContentLoaded', async () => {
    // fetch publishable key and init stripe
    const {publishableKey} = await fetch("/payments/config").then(r => r.json())
    const stripe = Stripe(publishableKey)

    // fetch client secret and init elements
    const {clientSecret} = await fetch("/payments/process_payment", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(r => r.json())
    let emailAddress
    // const addressOpts = { mode: 'shipping'}
    const elements = stripe.elements({clientSecret})
    const linkAuthElement = elements.create("linkAuthentication")
    linkAuthElement.mount("#link-authentication-element")
    linkAuthElement.on('change', (event) => {
        emailAddress = event.value.email
    })
    // const addressElement = elements.create('address', addressOpts)
    // addressElement.mount('#address-element')
    const paymentElementOpts = { layout: 'tabs' }
    const paymentElement = elements.create('payment', paymentElementOpts)
    paymentElement.mount('#payment-element')

    const form = document.getElementById('payment-form')
    form.addEventListener('submit', async(e) => {
        e.preventDefault();

        const {error} = await stripe.confirmPayment({
            elements,
            confirmParams: {
                return_url: 'http://192.168.0.22:5000/payments/success'
            }
        })
        if(error) {
            const messages = document.getElementById('payment-message')
            messages.innerText = error.message;
        }
    })
})