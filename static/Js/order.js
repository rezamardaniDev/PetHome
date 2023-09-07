function addProductToOrder(productId) {
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + 1).then(res => {
        if (res.status == 'success') {
            Swal.fire({
                position: 'top-center',
                icon: 'success',
                title: 'محصول به سبد خرید افزوده شد',
                showConfirmButton: false,
                timer: 1200
            })
        }
    });
}

function removeOrderDetail(detailID){
    $.get('/user/delete-order-detail?detail_id=' + detailID).then(res => {
        if (res.status == 'success'){
            $('#order-detail-content').html(res.body);
        }
    })

}


function changeOrderDetialCount(detailId, state){
    $.get('/user/change-order-detail?detail_id=' + detailId + '&state=' + state ).then(res =>{
        console.log(detailId, state);
    })
}