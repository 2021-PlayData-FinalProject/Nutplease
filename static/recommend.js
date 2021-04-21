$(function () {
    const source = document.getElementById('autoComplete');
    const inputHandler = function (e) {
        if (e.target.value == "") {
            $('.searchButton').attr('disabled', true);
        } else {
            $('.searchButton').attr('disabled', false);
        }
    }
    source.addEventListener('input', inputHandler);

    $('.searchButton').on('click', function () {
        var my_api_key = 'b829e26dcf6505507be2efab4980934c';
        var title = $('.movie').val();
        if (title == "") {
            $('.results').css('display', 'none');
        } else {
            load_details(my_api_key, title);
        }
    });
});

function recommendcard(e) {
    var my_api_key = 'b829e26dcf6505507be2efab4980934c';
    var title = e.getAttribute('title');
    load_details(my_api_key, title);
}

function load_details(my_api_key, title) {
    $.ajax({
        type: 'GET',
        url: 'https://api.themoviedb.org/3/search/movie?api_key=' + my_api_key + '&query=' + title,
        success: function (movie) {
            if (movie.results.length < 1) {
                $('.results').css('display', 'none');
                $("#loader")
                    .delay(500)
                    .fadeOut();
            } else {
                $("#loader").fadeIn();
                $('.results')
                    .delay(1000)
                    .css('display', 'block');
                var movie_id = movie
                    .results[0]
                    .id;
                var movie_title = movie
                    .results[0]
                    .original_title;
                movie_recs(movie_title, movie_id, my_api_key);
            }
        },
        error: function () {
            alert('Invalid Request');
            $("#loader")
                .delay(500)
                .fadeOut();
        }
    });
}

function movie_recs(movie_title, movie_id, my_api_key) {
    $.ajax({
        type: 'GET',
        url: "/movie",
        data: {
            title: movie_title
        },
        success: function (recs) {
            if (recs == "This Content does not exist in the DataBase") {
                $('.results').css('display', 'none');
                $("#loader")
                    .delay(500)
                    .fadeOut();
            } else {
                $('.results').css('display', 'block');
                var movie_arr = recs;
                var arr = [];
                for (const movie in movie_arr) {
                    arr.push(movie_arr[movie]);
                }
                get_movie_details(movie_id, my_api_key, arr, movie_title);
            }
        },
        error: function () {
            alert("error recs");
            $("#loader")
                .delay(500)
                .fadeOut();
        }
    });
}

function get_movie_details(movie_id, my_api_key, arr, movie_title) {
    $.ajax({
        type: 'GET',
        url: 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_api_key,
        success: function (movie_details) {
            show_details(movie_details, arr, movie_title, my_api_key, movie_id);
        },
        error: function () {
            alert("API Error!");
            $("#loader")
                .delay(500)
                .fadeOut();
        }
    });
}

function show_details(movie_details, arr, movie_title, my_api_key) {
    var imdb_id = movie_details.imdb_id;
    var poster = 'https://image.tmdb.org/t/p/w500/' + movie_details.poster_path;
    var overview = movie_details.overview;
    var genres = movie_details.genres;
    var rating = movie_details.vote_average;
    var vote_count = movie_details.vote_count;
    var release_date = new Date(movie_details.release_date);
    var runtime = parseInt(movie_details.runtime);
    var status = movie_details.status;
    var genre_list = []
    for (var genre in genres) {
        genre_list.push(genres[genre].name);
    }
    var my_genre = genre_list.join(", ");
    if (runtime % 60 == 0) {
        runtime = Math.floor(runtime / 60) + " hour(s)"
    } else {
        runtime = Math.floor(runtime / 60) + " hour(s) " + (
            runtime % 60
        ) + " min(s)"
    }

    arr_poster = get_movie_posters(arr, my_api_key);

    details = {
        'title': movie_title,
        'imdb_id': imdb_id,
        'poster': poster,
        'genres': my_genre,
        'overview': overview,
        'rating': rating,
        'vote_count': vote_count.toLocaleString(),
        'release_date': release_date
            .toDateString()
            .split(' ')
            .slice(1)
            .join(' '),
        'runtime': runtime,
        'status': status,
        'rec_movies': JSON.stringify(arr),
        'rec_posters': JSON.stringify(arr_poster)
    }

    $.ajax({
        type: 'POST',
        data: details,
        url: "/recommend",
        dataType: 'html',
        complete: function () {
            $("#loader")
                .delay(500)
                .fadeOut();
        },
        success: function (response) {
            $('.results').html(response);
            $('#autoComplete').val('');
            $(window).scrollTop(0);
        }
    });
}

function get_movie_posters(arr, my_api_key) {
    var arr_poster_list = []
    for (var m in arr) {
        $.ajax({
            type: 'GET',
            url: 'https://api.themoviedb.org/3/search/movie?api_key=' + my_api_key + '&query=' + arr[m],
            async: false,
            success: function (m_data) {
                arr_poster_list.push(
                    'https://image.tmdb.org/t/p/w500/' + m_data.results[0].poster_path
                );
            },
            error: function () {
                alert("Invalid Request!");
                $("#loader")
                    .delay(500)
                    .fadeOut();
            }
        })
    }
    return arr_poster_list;
}