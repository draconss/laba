var shab = `<div class="panel-body">
 <div class="media-block">
 <a class="media-left" href="#"><img class="img-circle img-sm" alt="Профиль пользователя" src="http://bootstraptema.ru/snippets/icons/2016/mia/1.png"></a>
 <div class="media-body">
 <div class="mar-btm">
 <a href="#" class="btn-link text-semibold media-heading box-inline">{name}</a>
 <p class="text-muted text-sm"><i class="fa fa-mobile fa-lg"></i>{data}</p>
 </div>
 <p>{text}</p>
 <div class="pad-ver">
 <div class="btn-group">
 <a class="btn btn-sm btn-default btn-hover-success" href="#"><i class="fa fa-thumbs-up"></i></a>
 <a class="btn btn-sm btn-default btn-hover-danger" href="#"><i class="fa fa-thumbs-down"></i></a>
 </div>
 </div>`

function comen() {

        var text = $("#this_c").val();
        var data = new Date().toLocaleString('ru', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute:'numeric',
      });
        shab = shab.replace("{name}",name);
        shab = shab.replace("{data}",data);
        $("#sitr").append(shab.replace("{text}",text));
        $("#this_c").val("");
}



$(document).ready(function () {
    form = $("#form_test");
    $('#add').click(function () {
        var data_c = {};
        data_c["user"] = user_id;
        data_c["manga"] = manga_id;
        data_c["text"] = $("#this_c").val();
        var csrf_token = $('#form_test [name="csrfmiddlewaretoken"]').val();
         data_c["csrfmiddlewaretoken"] = csrf_token;
        $.ajax({
           url: "/coment/",
            type: "POST",
           data:  data_c,
            cache: true,
            success: function (data) {
				console.log(data);
                comen()
            }
        });

        })

});








