function addProductToOrder(productId) {
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + 1).then(res => {
        console.log(res)
    });
}

Swal.fire({
    position: 'top-center',
    icon: 'success',
    title: 'محصول به سبد خرید افزوده شد',
    showConfirmButton: false,
    timer: 1200
})