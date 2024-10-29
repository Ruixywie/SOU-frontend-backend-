<template>
    <div v-for="item in modules" :key="item.id" class="module-container">
        <div class="module">
        <img :src="item.poster" class="poster" alt="海报" />
        <div class="intro">
            <div class="intro-big">{{ item.title }}</div>
            <div class="intro-small">{{ item.subtitle }}</div>
        </div>
        </div>
        <div class="module-text">
        <a class="icon" :href="item.link">
            <div class="layer">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span class="icon-cover">
                <img :src="item.icon" class="cover" alt="图标" />
            </span>
            </div>
            <div class="module-text">{{ item.title }}</div>
        </a>
        </div>
    </div>
</template>

<script>
export default {
  name: 'LinkModule',
  props: {
    modules: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.module-container {
    position: relative;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 17px;
    border-radius: 10px;
}
.module {
    display: flex;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s;
    border-radius: 15px 25px;
    box-shadow: 0px -3px 5px rgba(0, 0, 0, 0.25);
    overflow: hidden;
}
.module-container:hover .module {
    top: -280px;
    opacity: 1;
}
.icon {
    text-decoration: none;
    color: #fff;
    display: block;
    position: relative;
}
.layer {
    width: 80px;
    height: 80px;
    transition: transform 0.3s;
}
.icon:hover .layer {
    transform: rotate(-35deg) skew(20deg);
}
.layer span {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    border: 1px solid #fff;
    border-radius: 15px;
    transition: all 0.3s;
}
.layer span,
.module-text {
    color: #ffffff;
    font: 100 25px '程荣光刻楷';
    text-shadow: 0 2px 5px rgba(0,0,0,0.4);
    white-space: nowrap; /* 防止文本换行 */
    letter-spacing: 4px; /* 字符间距 */
}
.icon .module-text {
    position: absolute;
    left: 50%;
    bottom: -5px;
    opacity: 0;
    font-weight: 500;
    transform: translateX(-50%);
    transition: bottom 0.3s ease, opacity 0.3s ease;
}
.icon:hover .module-text {
    bottom: -45px;
    opacity: 1;
}
.icon:hover .layer span:nth-child(1) {
    opacity: 0.2;
    transform: translate(-4px, 4px);
}
.icon:hover .layer span:nth-child(2) {
    opacity: 0.4;
    transform: translate(2px, -2px);
}
.icon:hover .layer span:nth-child(3) {
    opacity: 0.6;
    transform: translate(8px, -8px);
}
.icon:hover .layer span:nth-child(4) {
    opacity: 0.8;
    transform: translate(14px, -14px);
}
.icon:hover .layer span:nth-child(5) {
    opacity: 1;
    transform: translate(20px, -20px);
}
.icon-cover {
    font-size: 25px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.intro {
    position: absolute;
    bottom: 0;
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin: 10px 20px 50px 20px;
    color: #fff;
    white-space: nowrap; /* 防止文本换行 */
    z-index: 1;
}
.poster {
    width: 250px;
    height: 280px;
    object-fit: cover;
    object-position: 50% 0%;
    /* 添加渐变透明效果 */
    mask-image: linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 40%);
}
.intro-big {
    color: #ffffff;
    font: 100 20px '程荣光刻楷';
    text-shadow: 0 0 5px rgba(0,0,0,0.8);
}
.intro-small {
    color: #ffffff;
    font: 100 18px '程荣光刻楷';
    text-shadow: 0 0 5px rgba(0,0,0,0.8);
}
.cover {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 15px;
}
</style>
