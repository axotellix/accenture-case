
<!-- [ TEMPLATE ] -->
<template>
    <div class = 'header'>

        <!-- account state -->
        <HeaderCard title="Мой счет">
            <p class="mark">
                <span class = 'f-lite char-space-right'>&#8381;</span>
                27 820
            </p>
            <Button class="button purple">
                <Ico type="plus" />
            </Button>
        </HeaderCard>

        <!-- account state -->
        <HeaderCard title="Мой портфель">
            <p class="mark text-green">
                <span class = 'f-lite char-space-right'>&#8381;</span>
                42 119
                <span class = 'offset'>( + 7.7% )</span>
            </p>
        </HeaderCard>

        <!-- account state -->
        <HeaderCard title="Доходность">
            <div class = 'flex-column'>
            <div class="row text-green">
                <span class = 'text-key'>Доход</span>
                <span class = 'text-val'>
                    42 119
                    <span class = 'offset'>( + 10% )</span>
                </span>
            </div>
            <div class="row">
                <span class = 'text-key'>Цель</span>
                <span class = 'text-val'>
                    37 200
                    <span class = 'offset'>( + 7.7% )</span>
                </span>
            </div>
            </div>
        </HeaderCard>

        <!-- account state -->
        <HeaderCard title="Статус портфеля">
            <p class="mark">
                <span class = 'f-normal text-red'>Есть замечания</span>
            </p>
            <Button class="button red" @click="$emit('setPage', 'CaseStatus')">
               <Ico type="arrow-right" />
            </Button>
        </HeaderCard>

    </div>
</template>


<!-- [ SCRIPTS ] -->
<script>
import HeaderCard from './../HeaderCard'
import Button from './../Button'
import Ico from './../Ico'

export default {
    // [ Component name ]
    name: 'Header',

    // [ Child components ]
    components: {
        HeaderCard,
        Button,
        Ico,
    },

    // [ Emits ]
    emits: ['setPage'],

    // [ Methods ]
    methods: {
        setPage() {
            this.$emit('setPage', 'CaseStatus');
        }
    }
}
</script>

