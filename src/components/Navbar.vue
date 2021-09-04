
<!-- [ TEMPLATE ] -->
<template>
    <nav class='navbar'>

        <!-- navigation items -->
        <ul>
            <li class = 'menu-item active'><a href="">Мой портфель</a></li>
            <li class = 'menu-item'><a href="">Обзор активов</a></li>
            <li class = 'menu-item'><a href="">Мой профиль</a></li>
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
        msg: String
    }
}
</script>

