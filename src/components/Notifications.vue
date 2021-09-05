
<!-- [ TEMPLATE ] -->
<template>
    <nav class='notifications'>

        <div class="notifications-title">
            <!-- ico: bell -->
            <Ico type='bell' />
            <!-- heading -->
            <p class = 'heading'>Уведомления</p>
        </div>

        <!-- navigation items -->
        <ul>
            <li class = 'menu-item new'><a href="">Рекомендации</a></li>
            <li class = 'menu-item'><a href="">Новости</a></li>
        </ul>

    </nav>
</template>


<!-- [ SCRIPTS ] -->
<script>
import Ico from './Ico'

export default {
    // [ Component name ]
    name: 'Notifications',

    // [ Child components ]
    components: {
        Ico,
    },

    // [ Properties ]
    props: {
        msg: String
    }
}
</script>

