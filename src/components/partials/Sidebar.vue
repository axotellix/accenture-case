
<!-- [ TEMPLATE ] -->
<template>
    <div class='sidebar'>

        <!-- personal data -->
        <!-- <Avatar :src="this.person.avatar" :caption="this.person.caption" /> -->
        <Avatar />

        <!-- navigation bar -->
        <Navbar />

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
        msg: String
    }
}
</script>

