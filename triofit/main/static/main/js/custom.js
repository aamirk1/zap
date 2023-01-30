$(document).ready(function() {
    $('.increment-btn').click(function(e){
        e.preventDefault();
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value) ? 0: value;
        if(value < 10){
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function(e){
        e.preventDefault();
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0: value;
        if(value>1){
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
    
    $('.addToCart').click(function(e){
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find(".prod_id").val();
        var product_qty = $(this).closest('.product_data').find(".qty-input").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method : "POST",
            url: "/add_to_cart",
            data: {
                "product_id":product_id,
                "product_qty":product_qty,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log(response);
                alertify.success(response.status)
                
            }
            
        });

    });


    $('.changeQuantity').click(function(e){
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find(".prod_id").val();
        var product_qty = $(this).closest('.product_data').find(".qty-input").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method : "POST",
            url: "/update-cart",
            data: {
                "product_id":product_id,
                "product_qty":product_qty,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                // alertify.success(response.status)
                $('.cartdata').load(location.href +" .cartdata");
            }
        });

    });

    $(document).on('click','.dalete-cart-item',function(e){
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find(".prod_id").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method : "POST",
            url: "/deletecartitem",
            data: {
                "product_id":product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log('delete')
                $('.cartdata').load(location.href +" .cartdata");
                alertify.success(response.status)    
            }
        });
    });

    $(document).on('click','.dalete-wishlist-item',function(e){
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find(".prod_id").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method : "POST",
            url: "/deletewishlistitem",
            data: {
                "product_id":product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log('delete')
                $('.wishdata').load(location.href +" .wishdata");
                alertify.success(response.status)    
            }
        });

    });

    $('.addToWishlist').click(function(e){
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find(".prod_id").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method : "POST",
            url: "/add_to_wishlist",
            data: {
                "product_id":product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log(response);
                
                alertify.success(response.status)
                
            }
            
        });

    });
    
      document.querySelector('html').classList.remove('no-js');
      if (!window.Cypress) {
        const scrollCounter = document.querySelector('.js-scroll-counter');

        AOS.init({
          mirror: true
        });

        document.addEventListener('aos:in', function(e) {
          console.log('in!', e.detail);
        });

        window.addEventListener('scroll', function() {
          scrollCounter.innerHTML = window.pageYOffset;
        });
      }
    
});

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }