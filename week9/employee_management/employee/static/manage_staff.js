function addStaff(project_id, csrf_token ){
    const emp = document.getElementById('input-add-staff');
    const emp_id = emp.value;
        
    fetch(`/employee/project/${project_id}/add_staff/${emp_id}/`, {
        method: 'PUT',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf_token,
        },
        body: JSON.stringify({ 'emp_id': parseInt(emp_id) })
    })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log('Employee added successfully');
                window.location.reload();
            } else {
                console.error('Error:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));
}

async function removeStaff(project_id, emp_id, csrf_token ){
    // กำหนด path ให้ถูกต้อง
    fetch(`/employee/project/${project_id}/delete_staff/${emp_id}/`, {
        method: 'DELETE',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf_token,
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}