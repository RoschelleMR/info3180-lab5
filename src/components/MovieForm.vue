<template>
    <form @submit.prevent="saveMovie" id='movieForm'> 

        <label for="title" class="form-label">Title</label>
        <input type="text" name="title" class="formcontrol" />

        <label for="desc" class="form-label">Desciption</label>
        <input type="text" name="desc" class="formcontrol" />

        <label for="poster" class="form-label">Poster</label>
        <input 
            type="file" 
            name="poster"
            class="formcontrol" 
            accept=".jpg, .jpeg, .png, .gif"/>

        <input type="submit" value="Submit">
        
    </form>
</template>

<script setup>

    import { ref, onMounted } from "vue"; onMounted(() => {     
        getCsrfToken(); 
    }); 

    let csrf_token = ref("");  

    function getCsrfToken() {     
        fetch('/api/v1/csrf-token')       
        .then((response) => response.json())       
        .then((data) => {         
            console.log(data);         
            csrf_token.value = data.csrf_token;       
        })   
    } 

    const saveMovie = () =>{

        let movieForm = document.getElementById('movieForm'); 
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {     
            method: 'POST', 
            body: form_data,
            headers: {             
                'X-CSRFToken': csrf_token.value         
                }  
            })     
            .then(function (response) {         
                return response.json();     
            })     
            .then(function (data) {         
                // display a success message         
                console.log(data, 'Success');     
            })     
            .catch(function (error) {         
                console.log(error, 'Error');     
            });
    }
</script>