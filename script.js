function edit(id){
    const row = document.getElementById(id);
    const viewElements = row.querySelectorAll(".view_mode");
    const editElements = row.querySelectorAll(".edit_mode");

    viewElements.forEach(el => el.style.display = 'none');
    editElements.forEach(el => el.style.display = 'inline-block');
}