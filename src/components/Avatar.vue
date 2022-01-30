
<!-- [ TEMPLATE ] -->
<template>
    <div class='avatar'>

        <!-- img: person avatar -->
        <div class='ava-img'><img :src="'/img/avatars/' + active_user + '.png'" alt="avatar"></div>

        <!-- caption: person name -->
        <p class='caption'>{{ this.name || 'Name Name' }}</p>

    </div>
</template>


<!-- [ SCRIPTS ] -->
<script>

export default {
    // [ Component name ]
    name: 'Avatar',

    // [ Properties ]
    props: {
        name: {
            type: String,
            default: 'Name Name'
        },
        active_user: {
            type: String,
            default: 'user1'
        },
        ava: String,
    }
}
</script>

