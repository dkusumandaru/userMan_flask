$(document).ready(function(){
    $('#application').on('click','.edit_record',function(){

      $('#idEdit').val('');
      var id=$(this).data('id');
      var name=$(this).data('name');
      $('#edit [name="id"]').val(id);
      $('#edit [name="name"]').val(name);
      $('#edit').modal('show');
      // $('#edit').submit();
    });


    $('#item').on('click','.remove_record',function(){

      $('#idRemove').val('');
      var url=$(this).data('url');
      var id=$(this).data('id');
      var name_warga=$(this).data('name_warga');

      $('#removeModalForm').attr("action",url);
      $('#idRemove').val(id);

      Swal.fire({
        title: 'Are you sure to delete warga <b> '+name_warga+'</b> ?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.isConfirmed) {
          $('#removeModalForm').submit();
        }
      })

    });
  });