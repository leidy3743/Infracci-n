function listeners(){
  /* Incializacion DataTable */
  $('.table').DataTable();
  /* Creacion de peaje */
  $("body").on('click', "#btn-nuevo", function(event){
      event.preventDefault();

      var $form = $("form");
      $form.attr('action','/peaje/crear');
      $("#peaje-modal-title").html("Nuevo Peaje");
      $("#submit").show();

      $.ajax({
          type: 'GET',
          url: $form.attr('action'),
          dataType: 'json',
          success: function (data) {

              $("#peaje-modal-body").html(data.html);
              $("#peaje-modal").modal("toggle");
          },
          error: error
      });
  });

  /* Actualización de peaje */
    $("body").on('click',".update", function(event){
      event.preventDefault();

      var $form = $("form");
      $form.attr('action',$(this).attr("href"));
      $("#peaje-modal-title").html("Actualizar Peaje");
      $("#submit").show();

      $.ajax({
          type: 'GET',
          url: $(this).attr("href"),
          dataType: 'json',
          success: function (data) {

              $("#peaje-modal-body").html(data.html);
              $("#peaje-modal").modal("toggle");
          },
          error: error
      });
  });

  /* submit del formulario */
  $("#submit").click(function(event){
      event.preventDefault();
      var $form = $("form");
      $form.ajaxSubmit({
          url: $form.attr('action'),
          dataType: 'json',
          success: function(response, status, xhr, $form) {
              if(response.status==true){
                  $("#section-content").html(response.html);
                  $('.table').DataTable();
                  $("#peaje-modal").modal("toggle");
              }else{
                  $("#peaje-modal-body").html(response.html);
              };
          },
          error: error
      });
  });

  /* Aviso de error  */
  var error = function (data) {
      var html = '<div class="alert alert-danger fade in m-b-15"> \
                      <strong>Error!</strong> \
                          Se ha presentado un error al intentar obtener información del servidor, \
                          por favor verifique el archivo apps.peaje.js \
                      <span class="close" data-dismiss="alert">&times;</span> \
                  </div>';

      $("#modal-footer").html(html);
      $("#dialog").modal("toggle");

  }
}

$(document).ready(function(){
  listeners();
});