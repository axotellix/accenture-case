
<!-- [ TEMPLATE ] -->
<template>
    <div class='modal'>

        <!-- [ modal overlay ] -->
        <div class = 'modal-overlay' @click="$emit('selectUserModal', 'false')"></div>

        <!-- [ modal content ] -->
        <ul class = 'modal-content'>
            <h2 class = 'title'>Выберите пользователя:</h2>
            <li class = 'option' :class='active_user == "user1" ? "active" : ""' @click="$emit('setUser', 'user1')"><span>Dastin Coleman [Консервативный]</span></li>
            <li class = 'option' :class='active_user == "user2" ? "active" : ""' @click="$emit('setUser', 'user2')"><span>Shaun Harrison [Умеренный]</span></li>
            <li class = 'option' :class='active_user == "user3" ? "active" : ""' @click="$emit('setUser', 'user3')"><span>Stephen Edwards [Консервативный]</span></li>
        </ul>

    </div>
</template>


<!-- [ SCRIPTS ] -->
<script>

export default {
    // [ Component name ]
    name: 'SelectUser',

    // [ Properties ]
    props: {
        active_user: String
    },

    // [ emits ]
    emits: ['setUser', 'selectUserModal'],

    // [ methods ]
    methods: {
        // setUser( user ) {
        //     this.person.name = user
        // }
    },

    // [ on: create ]
    async created() {
        // get > person data

    }
}
</script>