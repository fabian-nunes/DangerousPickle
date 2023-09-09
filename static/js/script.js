function checkField() {
    let code = document.getElementById("code").value;
    if (code.length === 0) {
        Swal.fire(
          'Error!',
          'Field cannot be empty!',
          'error'
        )
        return false;
    }

    //get request to /access?code=code
       fetch("http://localhost:5000/access?code=" + code)
    .then(response => {
        if (response.status === 200) {
            return response.text(); // Read the response body as text
        } else {
            return response.text().then(errorMessage => {
                throw new Error(errorMessage); // Handle non-200 status codes
            });
        }
    })
    .then(data => {
        Swal.fire(
            'Success!',
            data,
            'success'
        );
    })
    .catch(error => {
        console.error('Fetch error:', error);
        Swal.fire(
          'Error!',
          'An error occurred while fetching data.',
          'error'
        );
    });
}