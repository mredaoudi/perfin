function deleteModel(id, model) {
    if (confirm('Are you sure you want to delete this?')) {
      var form = document.getElementById('delete-form');
      form.action = `/${model}/${id}/delete/`;
      form.submit();
    }
}
