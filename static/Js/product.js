function addOrder(productId) {
    $.get('/products/add-order?product_id=' + productId).then(res =>{
        console.log(res.status)
        if (res.status === 'success') {
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 7500,
                timerProgressBar: true,
                didOpen: (toast) => {
                  toast.addEventListener('mouseenter', Swal.stopTimer)
                  toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
            })
            Toast.fire({
                icon: res.icon,
                title: res.text
            })
        } else if(res.status === 'error') {
            Swal.fire({
                icon: res.icon,
                title: 'خطا!',
                text: res.text,
            })
        }
    })
}