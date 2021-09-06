
<!-- [ TEMPLATE ] -->
<template>
    <nav class='navbar'>

        <!-- navigation items -->
        <ul>
            <li class = 'menu-item' 
                :class="this.page == 'Home' ? 'active' : ''"
                @click="$emit('setPage', 'Home')"
            >
                Мой портфель
            </li>
            <li class = 'menu-item' :class="this.page == 'Overview' ? 'active' : ''">Обзор активов</li>
            <li class = 'menu-item' :class="this.page == 'Profile' ? 'active' : ''">Мой профиль</li>
        </ul>

    </nav>
</template>


<!-- [ SCRIPTS ] -->
<script>

export default {
    // [ Component name ]
    name: 'Navbar',

    // [ Properties ]
    props: {
        page: String
    },

    // [ emits ]
    emits: ['setPage']
}
</script>

