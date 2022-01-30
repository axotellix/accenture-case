
<!-- [ TEMPLATE ] -->
<template>
    <div class='sidebar'>

        <!-- personal data -->
        <Avatar :src="person.avatar" :name="person.name" :active_user="this.active_user" @click="$emit('selectUserModal', 'true')" />

        <!-- navigation bar -->
        <Navbar :page="this.page" @setPage="$emit('setPage', 'Home')" />

        <!-- notifications -->
        <Notifications />

        <!-- button: log out -->
        <Logout />

        <!-- img: logo -->
        <Logo />

    </div>
</template>


<!-- [ SCRIPTS ] -->
<script>
import Avatar from './../Avatar'
import Navbar from './../Navbar'
import Notifications from './../Notifications'
import Logout from './../Logout'
import Logo from './../Logo'

export default {
    // [ Component name ]
    name: 'Sidebar',

    // [ Child components ]
    components: {
        Avatar,
        Navbar,
        Notifications,
        Logout,
        Logo,
    },

    // [ Properties ]
    props: {
        page: String,
        active_user: String
    },

    // [ emits ]
    emits: ['setPage', 'selectUserModal'],

    // [ data ] 
    data() {
        return {
            person: {
                name: '',
                ava: ''
            }
        }
    },

    // [ on: create ]
    async created() {
        // get > person data
        let req = await fetch('https://axotellix.pythonanywhere.com/api/userinfo/' + this.active_user);
        let person = await req.json();

        this.person.name = person.name;
    }
}
</script>