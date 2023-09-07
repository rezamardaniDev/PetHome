function commentSend(post_id) {
    var text = $('#commentText').val();

    $.get(`/blog/${post_id}`, {
        message: text

    }).then(function (res) {
        $('#comment_block').html(res)
        $('#commentText').val('')
    });
}