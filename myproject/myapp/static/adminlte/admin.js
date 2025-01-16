const header_top = document.getElementById('header_top')
const header_top_con = document.getElementById('header_top_con');

const header_center = document.getElementById('header_center')
const header_center_con = document.getElementById('header_center_con');

const header_end = document.getElementById('header_end')
const header_end_con = document.getElementById('header_end_con');

const header_slider = document.getElementById('header_slider')
const header_slider_con = document.getElementById('header_slider_con');



const main_one_top = document.getElementById('main_one_top')
const main_one_top_con = document.getElementById('main_one_top_con');

const main_one_left = document.getElementById('main_one_left')
const main_one_left_con = document.getElementById('main_one_left_con');

const main_one_right = document.getElementById('main_one_right')
const main_one_right_con = document.getElementById('main_one_right_con');



const main_two_left = document.getElementById('main_two_left')
const main_two_left_con = document.getElementById('main_two_left_con');

const main_two_right = document.getElementById('main_two_right')
const main_two_right_con = document.getElementById('main_two_right_con');



const main_thee_top = document.getElementById('main_thee_top')
const main_thee_top_con = document.getElementById('main_thee_top_con');

const main_thee_content = document.getElementById('main_thee_content')
const main_thee_content_con = document.getElementById('main_thee_content_con');



const main_four_top = document.getElementById('main_four_top')
const main_four_top_con = document.getElementById('main_four_top_con');

const main_four_left = document.getElementById('main_four_left')
const main_four_left_con = document.getElementById('main_four_left_con');

const main_four_right = document.getElementById('main_four_right')
const main_four_right_con = document.getElementById('main_four_right_con');



const footer = document.getElementById('footer')
const footer_con = document.getElementById('footer_con');



const user = document.getElementById('user')
const user_con = document.getElementById('user_con');





const meetings = document.getElementById('meetings')
const meetings_con = document.getElementById('meetings_con');

const meeting_details = document.getElementById('meeting_details')
const meeting_details_con = document.getElementById('meeting_details_con');




// Показать таблицу
function hideAllTables() {
    header_top_con.hidden = true;
    header_center_con.hidden = true;
    header_end_con.hidden = true;
    header_slider_con.hidden = true;

    main_one_top_con.hidden = true;
    main_one_left_con.hidden = true;
    main_one_right_con.hidden = true;

    main_two_left_con.hidden = true;
    main_two_right_con.hidden = true;

    main_thee_top_con.hidden = true;
    main_thee_content_con.hidden = true;

    main_four_top_con.hidden = true;
    main_four_left_con.hidden = true;
    main_four_right_con.hidden = true;

    footer_con.hidden = true;

    user_con.hidden = true;

    meetings_con.hidden = true;
    meeting_details_con.hidden = true;
}

header_top.addEventListener('click', () => {
    hideAllTables();
    header_top_con.hidden = false;
});
header_center.addEventListener('click', () => {
    hideAllTables();
    header_center_con.hidden = false;
});
header_end.addEventListener('click', () => {
    hideAllTables();
    header_end_con.hidden = false;
});
header_slider.addEventListener('click', () => {
    hideAllTables();
    header_slider_con.hidden = false;
});



main_one_top.addEventListener('click', () => {
    hideAllTables();
    main_one_top_con.hidden = false;
});
main_one_left.addEventListener('click', () => {
    hideAllTables();
    main_one_left_con.hidden = false;
});
main_one_right.addEventListener('click', () => {
    hideAllTables();
    main_one_right_con.hidden = false;
});



main_two_left.addEventListener('click', () => {
    hideAllTables();
    main_two_left_con.hidden = false;
});
main_two_right.addEventListener('click', () => {
    hideAllTables();
    main_two_right_con.hidden = false;
});



main_thee_top.addEventListener('click', () => {
    hideAllTables();
    main_thee_top_con.hidden = false;
});
main_thee_content.addEventListener('click', () => {
    hideAllTables();
    main_thee_content_con.hidden = false;
});



main_four_top.addEventListener('click', () => {
    hideAllTables();
    main_four_top_con.hidden = false;
});
main_four_left.addEventListener('click', () => {
    hideAllTables();
    main_four_left_con.hidden = false;
});
main_four_right.addEventListener('click', () => {
    hideAllTables();
    main_four_right_con.hidden = false;
});



footer.addEventListener('click', () => {
    hideAllTables();
    footer_con.hidden = false;
});



user.addEventListener('click', () => {
    hideAllTables();
    user_con.hidden = false;
});



meetings.addEventListener('click', () => {
    hideAllTables();
    meetings_con.hidden = false;
});


meeting_details.addEventListener('click', () => {
    hideAllTables();
    meeting_details_con.hidden = false;
});