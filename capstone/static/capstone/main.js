// Edit game function
function edit(id) {
    let edit_description = document.querySelector(`#edit-description-${id}`);
    let edit_genre = document.querySelector(`#edit-genre-${id}`);
    let edit_platform = document.querySelector(`#edit-platform-${id}`);
    let edit_developer = document.querySelector(`#edit-developer-${id}`);
    let edit_publisher = document.querySelector(`#edit-publisher-${id}`);
    let edit_image = document.querySelector(`#edit-image-${id}`);

    let button_to_edit = document.querySelector('#edit');
    let edit_button = document.querySelector(`#edit-button-${id}`);

    let edit_alert = document.querySelector('#edit-alert');

    edit_description.style.display = 'block';
    edit_genre.style.display = 'block';
    edit_platform.style.display = 'block';
    edit_developer.style.display = 'block';
    edit_publisher.style.display = 'block';
    edit_image.style.display = 'block';

    button_to_edit.style.display = 'none';
    edit_button.style.display = 'block';

    edit_alert.style.display = 'none';

    edit_button.addEventListener('click', () => {
        fetch('/edit/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                description: edit_description.value,
                genre: edit_genre.value,
                platform: edit_platform.value,
                developer: edit_developer.value,
                publisher: edit_publisher.value,
                image: edit_image.value
            })
        });

        edit_description.style.display = 'none';
        edit_genre.style.display = 'none';
        edit_platform.style.display = 'none';
        edit_developer.style.display = 'none';
        edit_publisher.style.display = 'none';
        edit_image.style.display = 'none';

        button_to_edit.style.display = 'block';
        edit_button.style.display = 'none';

        edit_alert.style.display = 'block';


        document.querySelector(`#game-description-${id}`).innerHTML = edit_description.value;
        document.querySelector(`#game-genre-${id}`).innerHTML = edit_genre.value;
        document.querySelector(`#game-platform-${id}`).innerHTML = edit_platform.value;
        document.querySelector(`#game-developer-${id}`).innerHTML = edit_developer.value;
        document.querySelector(`#game-publisher-${id}`).innerHTML = edit_publisher.value;
        document.querySelector(`#game-image-${id}`).innerHTML = edit_image.value;
    });
    edit_description.value = edit_description.value;
    edit_genre.value = edit_genre.value;
    edit_platform.value = edit_platform.value;
    edit_developer.value = edit_developer.value;
    edit_publisher.value = edit_publisher.value;
    edit_image.value = edit_image.value;
};

// Delete game confirmation
function delete_confirmation() {
    return confirm("Are you sure you want to delete this game?");
};