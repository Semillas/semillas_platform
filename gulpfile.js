var gulp = require('gulp');
var sass = require('gulp-sass');
var cssnano = require('gulp-cssnano');
var imagemin = require('gulp-imagemin');
var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync').create();

gulp.task('default', ['css'], function() {
	browserSync.init({
		//server: "./app"
	});

	gulp.watch("semillas_backend/static/sass/**/*.scss", ['css']);
});

gulp.task('semillas_backend/static/images', function() {
    	gulp.src('images/*')
		.pipe(imagemin())
		.pipe(gulp.dest('images'));
});

gulp.task('css', function(){
	return gulp.src('semillas_backend/static/sass/**/*.scss')
		.pipe(sass())
		.pipe(cssnano())
		.pipe(autoprefixer({
	browsers: ['last 4 versions'],
	cascade: false
	}))
		.pipe(gulp.dest('semillas_backend/static/css'))
		.pipe(browserSync.stream());
});