
<template>
    <ul>
        <div v-for="movie in movies">
            {{ movie.title }}
            {{ movie.desc }}
            <img v-bind:src="movie.poster" alt=""/>
        </div>
    </ul>
    
</template>

<script setup> 

    import { ref, onMounted } from "vue"; onMounted(() => {     
        fetchMovies(); 
    }); 

    let movies = ref([]);

    const fetchMovies = () =>{

        fetch('/api/v1/movies')       
        .then((response) => 
            response.json())
                   
        .then((data) => {         
            console.log(data);         
            movies.value = data.movies;    
        }) 

    }
</script> 