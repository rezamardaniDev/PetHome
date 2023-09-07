function commentSend(post_id) {
    var text = $('#commentText').val();

    $.get(`/blog/${post_id}`, {
        message: text

    }).then(function (res) {
        $('#comment_block').html(res)
        $('#commentText').val('')
    });
}

function commentSendProduct(product_id) {
    var text = $('#commentText').val();

    $.get(`/products/${product_id}`, {
        message: text

    }).then(function (res) {
        $('#comment_block').html(res)
        $('#commentText').val('')
    });
}