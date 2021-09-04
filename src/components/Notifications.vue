
<!-- [ TEMPLATE ] -->
<template>
    <nav class='notifications'>

        <!-- heading -->
        <p class = 'heading'>Уведомления</p>

        <!-- navigation items -->
        <ul>
            <li class = 'menu-item'><a href="">Рекомендации</a></li>
            <li class = 'menu-item'><a href="">Новости</a></li>
        </ul>

    </nav>
</template>


<!-- [ SCRIPTS ] -->
<script>

export default {
    // [ Component name ]
    name: 'Notifications',

    // [ Properties ]
    props: {
        msg: String
    }
}
</script>

