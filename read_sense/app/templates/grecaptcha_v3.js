grecaptcha.ready(function() {
      grecaptcha.execute('{{rec_key_v3}}', {action: '{{action}}'}).then(function(token) {
         $.ajax({
         url:"/verify/gr/v3/",
         async:true,
         data:JSON.stringify({"token":token}),
         method:"POST",
         contentType: 'application/json;charset=UTF-8',
         success:function(data){
            console.log(data)
            }
         })
      });
  });