$(document).ready(function(){
    var table = $('#user').DataTable();

    $('#user').on('click','.edit_record',function(){
      $('#edit [name="id"]').val('');
      var id=$(this).data('id');
      var name=$(this).data('name');
      var email=$(this).data('email');
      $('#edit [name="id"]').val(id);
      $('#edit [name="name"]').val(name);
      $('#edit [name="email"]').val(email);
      $('#edit').modal('show');
      // $('#edit').submit();
    });


    $('#add').on('click', '.save', function(){

      var modal = 'add';
      var data = getInput(modal);
      // console.log(data);
      var valuePush;
      var paramPush;
      
      if (data['status'] == true) {
        $('#'+modal).modal('hide');
        const dataArr = data['value'];
        // const nameArr = data['name'];
        const idArr = data['id'];
        valuePush = dataArr[0];
        paramPush = idArr[0];
        Swal.fire({
          title: 'Create',
          html: 'Are you sure to Create New <b>user : '+valuePush+'</b> ?',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Save'
        }).then((result) => {

          // console.log(result.isConfirmed);
          if (result.isConfirmed) {
            $('#'+modal+'-form').submit();
          }else{
            $('#'+modal).modal('show');
          }
        })

      }else{
        const idArr = data['id'];
        for (var i = 0; i < idArr.length; i++) {
          $('#'+idArr[i]).addClass('is-invalid');
          $('#'+idArr[i]).parent('div').addClass('has-danger');
          $('#'+idArr[i]).parent('div').removeClass('focused');
        }
      }
    });
  
    $('#edit').on('click', '.save', function(){

      var modal = 'edit';
      var data = getInput(modal);
      // console.log(data);
      var valuePush;
      // var paramPush;
      
      if (data['status'] == true) {
        $('#'+modal).modal('hide');
        const dataArr = data['value'];
        // const nameArr = data['name'];
        // const idArr = data['id'];
        valuePush = dataArr[1];
        // paramPush = nameArr[0];
        Swal.fire({
          title: 'Edit',
          html: 'Are you sure to Edit <b>user : '+valuePush+'</b> ?',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Save'
        }).then((result) => {
          if (result.isConfirmed) {
            $('#'+modal+'-form').submit();
          }else{
            $('#'+modal).modal('show');
          }
        })

      }else{
        // console.log('update failed');
        const nameArr = data['name'];
        for (var i = 0; i < nameArr.length; i++) {
          $('#'+modal+' [name="'+nameArr[i]+'"]').addClass('is-invalid');
          $('#'+modal+' [name="'+nameArr[i]+'"]').parent('div').addClass('has-danger');
          $('#'+modal+' [name="'+nameArr[i]+'"]').parent('div').removeClass('focused');
        }
      }
    });

    $('#user').on('click','.remove_record',function(){

      var id=$(this).data('id');
      var name=$(this).data('name');
      $('#remove [name="id"]').val('');
      $('#remove [name="id"]').val(id);

      Swal.fire({
        html: 'Are you sure to remove <b>user : '+name+'</b> ?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, remove it!'
      }).then((result) => {
        if (result.isConfirmed) {
          $('#remove').submit();
        }
      })

    });
  });