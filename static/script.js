$(document).ready(function () {
    $('#id_start_number').on('change', function () {
        var enteredStartNumber = $(this).val();
        var existingStartNumbers = $(this).data('existing-start-numbers').split(',');
        var startNumberMessage = $('#start-number-alert');

        if (enteredStartNumber !== null && existingStartNumbers.includes(enteredStartNumber)) {
            startNumberMessage.text('This start number is already taken.');
            $(this).val('');
        } else {
            startNumberMessage.text('');
        }
    });
});

function confirmDelete(signupId) {
    var confirmationText = document.getElementById('confirmation-text-' + signupId);

    // Submit the form
    document.getElementById('delete-form-' + signupId).submit();
}

function showConfirmation(signupId) {
    var confirmationText = document.getElementById('confirmation-text-' + signupId);

    // Show visibility of the confirmation text
    confirmationText.style.display = confirmationText.style.display === 'inline' ? 'none' : 'inline';
}