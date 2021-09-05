
<!-- [ TEMPLATE ] -->
<template>
    <nav class='navbar'>

        <!-- navigation items -->
        <ul>
            <li class = 'menu-item' 
                :class="this.page == 'Home' ? 'active' : ''"
            >
                <a href="">Мой портфель</a>
            </li>
            <li class = 'menu-item' :class="this.page == 'Overview' ? 'active' : ''"><a href="">Обзор активов</a></li>
            <li class = 'menu-item' :class="this.page == 'Profile' ? 'active' : ''"><a href="">Мой профиль</a></li>
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

    data() {
        //next_page: ''
    },

    // [ Methods ]
    methods: {
        setPage() {
            this.$emit('setPage', 'CaseStatus');
        }
    }
}
</script>

