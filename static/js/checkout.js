$(document).ready(function (){
    $('.razorpay').click(function (e) {
        e.preventDefault();
        var name = $("[name ='name']").val();
        var email = $("[name ='email']").val();
        var phone = $("[name ='phone']").val();
        var desc = $("[name ='desc']").val();
        var exampleCheck1 = $("[name ='exampleCheck1']").val();

        if(name == "" || email == "" || phone == "" || desc == "" || exampleCheck1 == false)

          {
            swal("Alert", "All Fields Are Required", "error");
            return false;
          }
          else
          var options = {
            "key": "rzp_test_jbxQpJu2jp7MFU", // Enter the Key ID generated from the Dashboard
            "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            "currency": "INR",
            "name": "Vidhigyaan",
            "description": "Test Transaction",
            "image": "https://example.com/your_logo",
            //"order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            "handler": function (response){
                alert(response.razorpay_payment_id);
                //alert(response.razorpay_order_id);
                //alert(response.razorpay_signature)
            },
            "prefill": {
                "name": name,
                "email": email,
                "contact": phone
            },  
            "notes": {
                "address": "Razorpay Corporate Office"
            },
            "theme": {
                "color": "#3399cc"
            }
        };
        var rzp1 = new Razorpay(options);
        rzp1.on('payment.failed', function (response){
               
              
                alert(response.error.metadata.payment_id);
        });
       
            rzp1.open();
    });

});