$('#deleteConfirmModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var deleteUrl = button.data('delete-url') // Extract info from data-* attributes
    var modal = $(this)
    modal.find('#deleteImageConfirmButton').attr('href', deleteUrl)
})
