// $(document).ready(function() {
//     $('#deleteConfirmModal').on('show.bs.modal', function (event) {
//         var button = $(event.relatedTarget); // Button that triggered the modal
//         var deleteUrl = button.data('delete-url'); // Extract info from data-* attributes
//         var modal = $(this);
//         modal.find('#deleteImageConfirmButton').attr('href', deleteUrl);
//     });
// });

console.log("Script loaded");


// $(document).ready(function () {
//     console.log("Document ready");
//
//     $('#deleteConfirmModal').on('show.bs.modal', function (event) {
//         event.preventDefault();
//         var button = $(event.relatedTarget); // Button that triggered the modal
//         var deleteUrl = button.data('delete-url'); // Extract info from data-* attributes
//         console.log("Delete URL: ", deleteUrl); // Check the URL in the console
//
//         var modal = $(this);
//         modal.find('#deleteImageConfirmButton').attr('href', deleteUrl);
//         console.log('script working')
//     });
// });

// $('#deleteConfirmModal').on('show.bs.modal', function (event) {
//     var button = $(event.relatedTarget); // Button that triggered the modal
//     console.log("Button: ", button); // Log the button object
//     var deleteUrl = button.data('delete-url'); // Extract info from data-* attributes
//     console.log("Delete URL: ", deleteUrl); // Check the URL in the console
//
//     var modal = $(this);
//     modal.find('#deleteImageConfirmButton').attr('href', deleteUrl);
// });

// $('#deleteConfirmModal').on('show.bs.modal', function (event) {
//     var modal = $(this);
//     modal.find('#deleteImageConfirmButton').attr('href', "/image/recipe/79/delete-image/19/");
// });


//
// $(document).ready(function () {
//     console.log("Document ready");
//
//     // On modal show, set the click event for the "Delete" button
//     $('#deleteConfirmModal').on('show.bs.modal', function (event) {
//         const button = $(event.relatedTarget); // Button that triggered the modal
//         const deleteUrl = button.data('delete-url'); // Extract info from data-* attributes
//         console.log("Modal triggered, Delete URL: ", deleteUrl);
//
//         // Bind click event to "Delete" button
//         $('#deleteImageConfirmButton').off('click').on('click', function(e) {
//             e.preventDefault(); // Prevent default action
//             console.log("Delete button clicked, URL: ", deleteUrl);
//             if (deleteUrl) {
//                 window.location.href = deleteUrl; // Redirect to the delete URL
//             }
//         });
//     });
// });

//
// $(document).ready(function () {
//     console.log("Document ready");
//
//     $('#deleteConfirmModal').on('show.bs.modal', function (event) {
//         const button = $(event.relatedTarget); // Button that triggered the modal
//
//         // Using jQuery's .data() method to retrieve the delete URL
//         const deleteUrl = button.data('delete-url');
//         console.log("Modal triggered, Delete URL: ", deleteUrl);
//
//         $('#deleteImageConfirmButton').off('click').on('click', function(e) {
//             e.preventDefault();
//             if (deleteUrl) {
//                 console.log("Redirecting to: ", deleteUrl);
//                 window.location.href = deleteUrl;
//             } else {
//                 console.log("No delete URL found");
//             }
//         });
//     });
// });

$(document).ready(function () {
    console.log("Document ready");

    $('#deleteConfirmModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget); // Button that triggered the modal
        const deleteUrl = button.siblings('.delete-url').val(); // Retrieve the delete URL
        console.log("Modal triggered, Delete URL: ", deleteUrl);

        $('#deleteImageConfirmButton').off('click').on('click', function(e) {
            e.preventDefault();
            if (deleteUrl) {
                console.log("Redirecting to: ", deleteUrl);
                window.location.href = deleteUrl;
            } else {
                console.log("No delete URL found");
            }
        });
    });
});



// $('#deleteConfirmModal').modal('show');