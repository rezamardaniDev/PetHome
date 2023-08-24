function addProductToOrder(productId){
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + 1).then(res =>{
        console.log(res)
    });
}